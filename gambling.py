from sopel import module, tools, formatting
import random
import time


@module.require_admin
@module.require_chanmsg
@module.commands("award")
def award_money(bot, trigger):
    """Bot admin uses the power of Admin Abuse to spawn money from nothing."""
    winner = trigger.group(3)

    try:
        amount = int(trigger.group(4))
    except TypeError:
        bot.reply("I need an amount of money to award.")
        return
    except ValueError:
        bot.reply("That's not a number...")
        return

    if not (winner and amount):
        bot.reply("I need a target and an amount.")
        return

    winner = tools.Identifier(winner)

    if winner not in bot.channels[trigger.sender].privileges:
        bot.reply("Please provide a valid user.")
        return

    currency_amount = bot.db.get_nick_value(
        winner, "currency_amount", 0) + amount
    bot.db.set_nick_value(winner, "currency_amount", currency_amount)
    bot.say("{} has ${}".format(winner, currency_amount))


@module.require_admin
@module.commands("nomoremoney")
def delete_money(bot, trigger):
    """Bot admin can make it so a user never had any money."""
    target = trigger.group(3)

    if not target:
        bot.reply("I need someone's wealth to eliminate.")
        return

    bot.db.delete_nick_value(target, "currency_amount")
    bot.say("{}'s wealth has been deleted from existence.".format(target))


@module.commands(r"\$")
def check_money(bot, trigger):
    """Check how much money you or another user has."""
    target = trigger.group(3) or trigger.nick

    if not target:
        bot.reply("How in the hell did you do this?")
        return

    currency_amount = bot.db.get_nick_value(target, "currency_amount")
    if currency_amount is not None:
        bot.say("{} has ${}".format(target, currency_amount))
    else:
        bot.say(
            "{} has never participated in the currency plugin.".format(target))


@module.commands("iwantmoney")
def init_money(bot, trigger):
    """Use this command to get money for the first time ever and participate in gambling and other fun activities!"""
    target = trigger.nick
    check_for_money = bot.db.get_nick_value(target, "currency_amount")
    if check_for_money is None:
        bot.db.set_nick_value(target, "currency_amount", 100)
        bot.say(
            "Congratulations! Here's $100 to get you started, {}.".format(target))


@module.commands("betflip", "bf")
@module.example(".bf 10 h")
def gamble_betflip(bot, trigger):
    """Wager X amount of money on (h)eads or (t)ails. Winning will net you double your bet."""
    # Check that user has actually gambled some amount of money.
    try:
        bet = int(trigger.group(3))
        gambler = trigger.nick
    except TypeError:
        bot.reply("I need an amount of money to bet.")
        return
    except ValueError:
        bot.reply("That's not a number...")
        return

    # Check if user has enough money to make the gamble...
    bet_check = bot.db.get_nick_value(gambler, "currency_amount")
    if bet_check is None:
        bot.reply(
            "You can't gamble yet! Please run the `.iwantmoney` command.")
        return
    if bet > bet_check:
        bot.reply(
            "You don't have enough money to make this bet. Try a smaller bet.")
        return

    # Check if user has actually bet (H)eads or (T)ails.
    user_choice = trigger.group(4)
    if user_choice in ["h", "t"]:

        heads_or_tails = ["heads", "tails"]

        if user_choice == "h":
            user_choice = "heads"

        if user_choice == "t":
            user_choice = "tails"

        # Flip coin and keep the gambler in suspense...
        flip_result = random.choice(heads_or_tails)
        bot.action("flips a coin...")
        time.sleep(1.5)

        if flip_result == user_choice:
            winnings = bet * 2
            new_balance = bet_check + bet
            bot.db.set_nick_value(
                gambler, "currency_amount", new_balance)
            bot.reply(
                "Congrats; the coin landed on {}. You won ${}! Your new balance is ${}.".format(
                    flip_result, winnings, new_balance))
            return
        else:
            new_balance = bet_check - bet
            bot.db.set_nick_value(
                gambler, "currency_amount", new_balance)
            bot.reply(
                "Sorry, the coin landed on {}. You lost ${}. Your new balance is ${}.".format(
                    flip_result, bet, new_balance))
            return
    else:
        bot.reply("I need you to bet on (h)eads or (t)ails.")
