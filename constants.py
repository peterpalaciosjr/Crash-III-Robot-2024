class Constants():
    def robot_base_constants(self):
        global LEFT_FRONT_CAN_ID, LEFT_REAR_CAN_ID, RIGHT_FRONT_CAN_ID, RIGHT_REAR_CAN_ID
        global LAUNCH_WHEEL_CAN_ID, FEEDER_WHEEL_CAN_ID, ROLLER_CLAW_CAN_ID, CLIMBER_CAN_ID
        
        global DIFFERENTIAL_DRIVE_CURRENT
        global LAUNCH_WHEEL_CURRENT, FEEDER_WHEEL_CURRENT, ROLLER_CLAW_CURRENT
        global LAUNCH_WHEEL_SPEED, FEEDER_WHEEL_SPEED, ROLLER_CLAW_SPEED

        global CLIMBER_CURRENT, CLIMBER_SPEED
        global LEFT_FRONT_SPEED, RIGHT_FRONT_SPEED

        global driver_controller_type, operator_controller_type

        LEFT_FRONT_CAN_ID = 1
        LEFT_REAR_CAN_ID = 2
        RIGHT_FRONT_CAN_ID = 3
        RIGHT_REAR_CAN_ID = 4
        LAUNCH_WHEEL_CAN_ID = 5
        FEEDER_WHEEL_CAN_ID = 6
        ROLLER_CLAW_CAN_ID = 7
        CLIMBER_CAN_ID = 8


        DIFFERENTIAL_DRIVE_CURRENT = 100
        DIFFERENTIAL_DRIVE_SPEED = 1

        LAUNCH_WHEEL_CURRENT, FEEDER_WHEEL_CURRENT, ROLLER_CLAW_CURRENT = (145, 145, 100)
        LAUNCH_WHEEL_SPEED, FEEDER_WHEEL_SPEED, ROLLER_CLAW_SPEED = (0, 0, 0)

        CLIMBER_CURRENT, CLIMBER_SPEED = (100, 0)

        driver_controller_type, operator_controller_type = ("PS4", "PS4")


    
    def autonomous_constants(self):
        global AUTONOMOUS_MODE
        AUTONOMOUS_MODE = "null"

        
