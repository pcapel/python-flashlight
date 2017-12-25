import batteries


class Flashlight:


    def __init__(self, *args, **kwargs):
        self.batteries = batteries


    def config(self, dict_arg, **kwargs):
        """
        Configure your flashlight!
        :log_to:
        :log_as:
        :log_format:
        :new_batteries:
        """
        pass


    def shine(fn):
        @self.batteries.wrapper(fn)
        @self.batteries.logger
        @self.batteries.timer
        @self.batteries.capture_args
        @self.batteries.capture_result
        def bulb(*args, **kwargs):
            return fn(*args, **kwargs)
        return bulb
