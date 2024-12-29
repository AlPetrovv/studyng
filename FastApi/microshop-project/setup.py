from contextlib import asynccontextmanager

from fastapi import FastAPI

################## LIFESPAN ##################
# lifespan can be used in FasAPI class or ApiRouter class
# lifespan - function that run before start and stop app
# before start - until yield, before stop - after yield
# asynccontextmanager - decorator that create async context manager
# before yield run __aenter__ and after yield run __aexit__


# create db before start app
@asynccontextmanager
async def lifespan(app: FastAPI):
    #  ######## before app start ############
    yield
    #  ############## before app stop ############
    ...
