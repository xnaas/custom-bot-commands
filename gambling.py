from sopel import module, tools, formatting
import random
import re
import time


def parse_money(number):
    number = number.replace(',', '').replace('$', '')
    if number.isdigit():
        return int(number)

    try:
        match = re.match('([\d.]+)([kmbt])', number)
        calc = {'k': 1e3, 'm': 1e6, 'b': 1e9, 't': 1e12}
        num, size = match.groups()
        return int(float(num) * calc[size])
    except:
        raise ValueError


@module.require_admin
@module.require_chanmsg
@module.commands("award")
def award_money(bot, trigger):
    """Bot admin uses the power of Admin Abuse to spawn money from nothing."""
    if trigger.sender == "#casino":
        try:
            amount = parse_money(trigger.group(3))
            winner = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to award.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (winner and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check for valid target to award money to.
        winner = tools.Identifier(winner)
        if winner not in bot.channels[trigger.sender].privileges:
            bot.reply("Please provide a valid user.")
            return

        award_amount = bot.db.get_nick_value(
            winner, "currency_amount", 0) + amount
        bot.db.set_nick_value(winner, "currency_amount", award_amount)
        bot.say("{} has ${:,}".format(winner, award_amount))
    else:
        bot.reply("This command can only be used in #casino")


@module.require_admin
@module.require_chanmsg
@module.commands("take")
def take_money(bot, trigger):
    """Bot admin takes (deletes) X amount of money from a user."""
    if trigger.sender == "#casino":
        try:
            amount = parse_money(trigger.group(3))
            loser = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to take.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (loser and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check for valid target to take money from.
        loser = tools.Identifier(loser)
        if loser not in bot.channels[trigger.sender].privileges:
            bot.reply("Please provide a valid user.")
            return

        take_amount = bot.db.get_nick_value(
            loser, "currency_amount", 0) - amount
        bot.db.set_nick_value(loser, "currency_amount", take_amount)
        bot.say("{} has ${:,}".format(loser, take_amount))
    else:
        bot.reply("This command can only be used in #casino")


@module.require_chanmsg
@module.commands("give")
def give_money(bot, trigger):
    """Give X amount of your money to another user."""
    if trigger.sender == "#casino":
        giver = trigger.nick
        try:
            amount = parse_money(trigger.group(3))
            target = trigger.group(4)
        except AttributeError:
            bot.reply("I need an amount and a target.")
            return
        except TypeError:
            bot.reply("I need an amount of money to give.")
            return
        except ValueError:
            bot.reply("That's not a number...")
            return

        if not (target and amount):
            bot.reply("I need an amount and a target.")
            return

        # Check if user has enough money to give away...
        give_check = bot.db.get_nick_value(giver, "currency_amount")
        if give_check is None:
            bot.reply(
                "You don't have any money to give away. Please run the `.iwantmoney` command.")
            return
        if amount > give_check:
            bot.reply(
                "You don't have that much money to give away. Try a smaller amount.")
            return

        # Check for valid target to give money to.
        target = tools.Identifier(target)
        if target not in bot.channels[trigger.sender].privileges:
            bot.reply("Please provide a valid user.")
            return

        give_amount = bot.db.get_nick_value(
            giver, "currency_amount", 0) - amount
        receive_amount = bot.db.get_nick_value(
            target, "currency_amount", 0) + amount
        # Take away the money from the giver.
        bot.db.set_nick_value(giver, "currency_amount", give_amount)
        # Give the money to the target/reciever.
        bot.db.set_nick_value(target, "currency_amount", receive_amount)
        bot.say(
            "{} gifted ${:,} to {}. {} now has ${:,} and {} has ${:,}.".format(
                giver,
                amount,
                target,
                giver,
                give_amount,
                target,
                receive_amount))
    else:
        bot.reply("This command can only be used in #casino")


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


@module.require_chanmsg
@module.commands(r"\$")
def check_money(bot, trigger):
    """Check how much money you or another user has."""
    if trigger.sender == "#casino":
        target = trigger.group(3) or trigger.nick

        if not target:
            bot.reply("How in the hell did you do this?")
            return

        currency_amount = bot.db.get_nick_value(target, "currency_amount")
        if currency_amount is not None:
            bot.say("{} has ${:,}".format(target, currency_amount))
        else:
            bot.say(
                "{} has never participated in the currency plugin.".format(target))
    else:
        bot.reply("This command can only be used in #casino")


@module.require_chanmsg
@module.commands("iwantmoney")
def init_money(bot, trigger):
    """Use this command to get money for the first time ever and participate in gambling and other fun activities!"""
    if trigger.sender == "#casino":
        target = trigger.nick
        check_for_money = bot.db.get_nick_value(target, "currency_amount")
        if check_for_money is None:
            bot.db.set_nick_value(target, "currency_amount", 100)
            bot.say(
                "Congratulations! Here's $100 to get you started, {}.".format(target))
    else:
        bot.reply("This command can only be used in #casino")


@module.require_chanmsg  # Forcing public claiming serves as a reminder to all.
@module.commands("timely")
def claim_money(bot, trigger):
    """Claim $150 every 24 hours. ($250 for first claim!)"""
    if trigger.sender == "#casino":
        claimer = trigger.nick

        check_for_money = bot.db.get_nick_value(claimer, "currency_amount")
        if check_for_money is None:
            bot.say("You can't do this yet! Please run the `.iwantmoney` command.")
            return

        now = time.time()

        check_for_timely = bot.db.get_nick_value(claimer, "currency_timely")
        if check_for_timely is None:
            bot.db.set_nick_value(claimer, "currency_timely", now)
            claim = check_for_money + 150
            bot.db.set_nick_value(claimer, "currency_amount", claim)
            bot.reply(
                "New balance: ${:,}. Don't forget to claim again in 24 hours!".format(claim))
            return

        check_24_hours = now - check_for_timely
        if check_24_hours >= 86400:
            bot.db.set_nick_value(claimer, "currency_timely", now)
            claim = check_for_money + 150
            bot.db.set_nick_value(claimer, "currency_amount", claim)
            bot.reply(
                "New balance: ${:,}. Don't forget to claim again in 24 hours!".format(claim))
            return
        else:
            bot.reply("It hasn't been 24 hours yet, greedy!")
    else:
        bot.reply("This command can only be used in #casino")


@module.commands("betflip", "bf")
@module.example(".bf 10 h")
@module.rate(user=3)
def gamble_betflip(bot, trigger):
    """Wager X amount of money on (h)eads or (t)ails. Winning will net you double your bet."""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = parse_money(trigger.group(3))
        except AttributeError:
            bot.reply("I need an amount of money to bet and (h)eads or (t)ails.")
            return
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
        if bet == 0:
            bot.reply("You can't bet nothing!")
            return

        # Check if user has actually bet (H)eads or (T)ails.
        user_choice = trigger.group(4)
        if user_choice in ["h", "t", "heads", "tails"]:

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
                    "Congrats; the coin landed on {}. You won ${:,}! Your new balance is ${:,}.".format(
                        flip_result, winnings, new_balance))
                return
            else:
                new_balance = bet_check - bet
                bot.db.set_nick_value(
                    gambler, "currency_amount", new_balance)
                bot.reply(
                    "Sorry, the coin landed on {}. You lost ${:,}. Your new balance is ${:,}.".format(
                        flip_result, bet, new_balance))
                return
        else:
            bot.reply("I need you to bet on (h)eads or (t)ails.")
    else:
        bot.reply("This command can only be used in #casino")


@module.commands("wheeloffortune", "wheel")
@module.example(".wheel 100")
@module.rate(user=30)
def gamble_wheel(bot, trigger):
    """Spin the Wheel of Fortune!"""
    if trigger.sender == "#casino":
        gambler = trigger.nick
        # Check that user has actually gambled some amount of money.
        try:
            bet = parse_money(trigger.group(3))
        except AttributeError:
            bot.reply("I need an amount of money to bet.")
            return module.NOLIMIT
        except TypeError:
            bot.reply("I need an amount of money to bet.")
            return module.NOLIMIT
        except ValueError:
            bot.reply("That's not a number...")
            return module.NOLIMIT

        # Check if user has enough money to make the gamble...
        bet_check = bot.db.get_nick_value(gambler, "currency_amount")
        if bet_check is None:
            bot.reply(
                "You can't gamble yet! Please run the `.iwantmoney` command.")
            return module.NOLIMIT
        if bet > bet_check:
            bot.reply(
                "You don't have enough money to make this bet. Try a smaller bet.")
            return module.NOLIMIT
        if bet == 0:
            bot.reply("You can't bet nothing!")
            return module.NOLIMIT

        # Take the user's money before continuing
        spend_on_bet = bet_check - bet
        bot.db.set_nick_value(gambler, "currency_amount", spend_on_bet)

        # Configure Wheel Spin Directions
        wheel_direction = ["֎", "֍"]
        pointer_direction = {
            "↗": 7,
            "→": 6,
            "↘": 5,
            "↓": 4,
            "↙": 3,
            "←": 2,
            "↖": 1,
            "↑": 0
        }

        # Get the result first
        wheel_result = random.choices(list(pointer_direction.keys()), weights=[
                                      0.1, 0.4, 0.5, 4, 10, 27, 38, 20], k=1)[0]
        multiplier = pointer_direction[wheel_result]
        winnings = bet * multiplier
        new_balance = spend_on_bet + winnings
        bot.db.set_nick_value(gambler, "currency_amount", new_balance)
        # Stress out the user with delay 😉
        bot.action(
            "spins the wheel...{0}{0}{0}".format(
                random.choice(wheel_direction)))
        time.sleep(4)
        bot.say(formatting.italic("The wheel slows to a stop..."))
        time.sleep(2)

        # Conditionals
        if multiplier == 0:
            bot.say(
                "The arrow is facing [{}]. {}x multiplier. You lost. New balance: ${:,}.".format(
                    wheel_result, multiplier, new_balance))
            return
        elif multiplier == 1:
            bot.say(
                "The arrow is facing [{}]. {}x multiplier. Same balance: ${:,}.".format(
                    wheel_result, multiplier, bet_check))
            return
        else:
            bot.say(
                "The arrow is facing [{}]. You won: {}x your money! (${:,}). Your new balance is: ${:,}.".format(
                    wheel_result,
                    multiplier,
                    winnings,
                    new_balance))
    else:
        bot.reply("This command can only be used in #casino")
