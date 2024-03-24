if __name__ == '__main__':
    import logging
    import os
    from calculator.calculator import Calculator
    from functions.loadCommands import load_command
    from functions.loadEnv import loadEnv
    import datetime

    current_date_iso = datetime.date.today().isoformat()

    logging.basicConfig(filename=f'calculator_{current_date_iso}.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Program started")

    loadEnv()

    try:
        debugText = os.getenv("DEBUG_MODE")
        debugFlag = debugText.lower() == 'true'
    except Exception as e:
        debugWarn = "Warning: 'DEBUG_MODE' environment variable was not found."
        logging.warning(f"{debugWarn}: {e}")
        debugFlag = False

    hr = "_" * 30

    calcInst = Calculator()

    command = load_command('menu')
    commandList = command.execute(None)

    if debugFlag:
        print("DEBUG MODE ENABLED")
        print(f"Debug Line - operandMap = {calcInst.operandMap_}")

    while True:
        userIn = input("Enter your command\n")
        logging.info(f"User input: {userIn}")

        if userIn.lower() in commandList:
            logging.info(f"Command executed: {userIn}")

            if debugFlag:
                print(f"Debug Line - executing command from commands/{userIn.lower()}.py")
            
            try:
                command = load_command(userIn)
                command.execute(calcInst)
                
            except Exception as e:
                print(e)
                logging.error(f"Command threw an error: {e}")
            print(hr)

        else:

            try:
                result = calcInst.ingest_operation(userIn)

            except AttributeError as e:
                print(e)
                logging.warning(f"User Input '{userIn}': {e}")
                continue

            except Exception as e:
                print(f"{e}")
                logging.error(f"Error from user input '{userIn}': {e}")
                continue           

            if debugFlag:
                print(f"Debug Line - Input cleaned to: {calcInst.x_} {calcInst.operandSymbol_} {calcInst.y_}")
                print(f"Debug Line - x: {calcInst.x_} | operand: {calcInst.operandSymbol_} | y: {calcInst.y_} | result: {result}")            

            print("Result:", result)
            logging.info("Operation performed: %s %s %s = %s", calcInst.x_, calcInst.operandSymbol_, calcInst.y_, result)
            print(hr)


