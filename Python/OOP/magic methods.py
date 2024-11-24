# Repeat magic methods for classes


#  first question: what is order of magic methods while object of class is creating?
#  second question: what is MRO and how to change order in MRO?
#  third question: how to create generator(iterator) from class?
#  fourth question: how to use attribute in class with magic methods?
#  fifth question: dict, str, list, etc. (which methods they use?)
#  sixth question: how to make class as opened and closed?
#  seventh question: what is magic attribute like __slots__, __module__, __doc__, etc.?
#  eighth question: what is difference between __str__ and __repr__?
class Class(object):
    # __class__ = None
    # __dict__ = {}
    # __doc__ = ''
    # __module__ = ''
    # __slots__ = ''
    # __bases__ = tuple()
    # __basicsize__ = 904
    # __dictoffset__ = 264
    # __flags__ = 2148031744
    # __itemsize__ = 40
    # __mro__ = tuple()
    # __weakrefoffset__ = 368


    ################################## NEW, INIT, CALL ##########################
    # __new__ - it method runs as first method when Class creates instance c = Class()
    # __new__ - exactly(именно) this method return the instance (self)
    # redefining it we can add some logic before creating the instance (self)
    # cls - "Class", self - instance of "Class"
    def __new__(cls, *args, **kwargs):
        #  __new__ can receive args and kwargs from c = Class(1, 2)
        print('Do smth before create instance (self)')
        print(f'args in __new__: {args} ||| kwargs in __new__ {kwargs}')

        # create instance without arguments into __new__ method, __init__ doesn't work yet
        instance = super().__new__(cls)

        print('Do smth after create instance (self)')
        # add instance attribute "x"
        instance.x = 'x'

        return instance # return instance

    #  __init__ - does not create the instance of class, that we name "self".
    #  __init__ - the constructor of instance, the instance created in  method __new__,
    #  __init__ construct (add attribute and do some logic if it there is).
    #  instance - separate entity that we can use, that is there is base class "Class",
    #  we create the instance of class then use this instance separately from base class
    def __init__(self, *args, **kwargs):
        print(f'args in __init__: {args}\nkwargs in __init__ {kwargs}')
        self.arg_1 = args[0]
        self.arg_2 = args[1]
        self.const = 10

    def __call__(self):
        print(f'this is __call__ function in "{self.__class__.__name__}" class')

#  ############################# END NEW, INIT, CALL #########################


    def __str__(self):
        return f'{self.arg_1}, {self.arg_2}, {self.const}, {self.x}'

    def __repr__(self):
        return f'__repr__ func in "{self.__class__.__name__}" class'

    # def __getitem__(self):
    #   ...

    # def __setitem__(self):
    #     ...

    def __del__(self):
        ...

    def __bool__(self):
        ...

    def __iter__(self):
        ...

    def __next__(self):
        ...

    # def __getattr__(self):
    #     ...

    # def __setattr__(self, name, value):
    #     ...

    def __delattr__(self, name):
        ...

    # def __getattribute__(self, name):
    #     ...

    def __hash__(self):
        ...

    def __divmod__(self, other):
        ...

    def __delete__(self, instance):
        ...

    def __enter__(self):
        ...

    def __exit__(self):
        ...

    def __mro_entries__(self, bases):
        ...

    def __mro__(self):
        ...

    # ## async magic methods
    async def __aenter__(self):
        ...

    async def __aexit__(self):
        ...

    async def __aiter__(self):
        ...

    async def __anext__(self):
        ...

    def __await__(self):
        ...

c = Class(1, 2)

# repr function will be run if you use "=".
print(f'{c=}')

# run __call__ function
c()

class NewClass:
    def __init__(self, *args, **kwargs):
        if len(args) < 2:
            return
        self.arg_1 = args[0]
        self.arg_2 = args[1]

#  What did you do?
#  __new__ method creates the instance of NewClass and return it, however __init__ method didn't work, why?
# Because in the beginning python start __call__ method then __new__ method that creates the instance. After python start __init__
# but if
nc = NewClass.__new__(NewClass)
print(f'{nc=}')
nc_2 = NewClass()


##################################### PATTERNS ##############################

# Singleton
class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


class Logger(Singleton):
    def __init__(self, path, *args, **kwargs):
        self.path = path


logger_1 = Logger('path_1')
logger_2 = Logger('path_2')
print(logger_1.path, logger_2.path, sep='\n')
print(logger_1, logger_2, sep='\n')
