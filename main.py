"""
Program for a simple calculator that can perform basic arithmetic operations.
"""
if __name__ == '__main__':
    import logging
    import os
    from calculator.calculator import Calculator
    from functions.load_commands import load_command
    from dotenv import load_dotenv
    import datetime

    current_date_iso = datetime.date.today().isoformat()

    log_filename = f'calculator_{current_date_iso}.log'
    logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Program started")

    load_dotenv()

    debug_mode = os.getenv("DEBUG_MODE")
    print(debug_mode)

    # Check if DEBUG_MODE is set
    if debug_mode is not None:
        # Convert the value to lowercase and check if it's 'true'
        DEBUG_FLAG = debug_mode.lower() == 'true'
    else:
        # If DEBUG_MODE is not set, assume DEBUG_FLAG as False and warn.
        DEBUG_FLAG = False
        logging.warning("No .env file was found in the application directory on launch.")


    HR = "_" * 30

    calcInst = Calculator()

    command = load_command('menu')
    commandList = command.execute(calcInst)

    if DEBUG_FLAG:
        print("DEBUG MODE ENABLED")
        print(f"Debug Line - operandMap = {calcInst.operand_map_}")

    while True:

        userIn = input("Enter your command\n")
        logging.info("User input: %s",userIn)

        if userIn.lower() in commandList:
            logging.info("Command executed: %s",userIn)

            if DEBUG_FLAG:
                print(f"Debug Line - executing command from commands/{userIn.lower()}.py")

            command = load_command(userIn)
            command.execute(calcInst)
            print(HR)

        else:

            try:
                result = calcInst.ingest_operation(userIn)

            except AttributeError as e:
                print(e)
                logging.warning("User Input '%s': %s", userIn, e)
                continue

            except ValueError as e:
                print(f"Invalid input: {e}")
                logging.error("Error from user input '%s': %s", userIn, e)
                continue

            except ZeroDivisionError as e:
                print("Division by zero is not allowed.")
                logging.error("Error from user input '%s': %s", userIn, e)
                continue


            if DEBUG_FLAG:
                print(f"Debug Line - Input cleaned to: "
                f"{calcInst.x_} {calcInst.operand_symbol_} {calcInst.y_}")

                print(f"Debug Line - x: {calcInst.x_} | "
                f"operand: {calcInst.operand_symbol_} | "
                f"y: {calcInst.y_} | result: {result}")


            print("Result:", result)
            logging.info("Operation performed: %s %s %s = %s",
             calcInst.x_, calcInst.operand_symbol_,
             calcInst.y_, result)

            print(HR)
