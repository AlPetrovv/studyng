How to process view in FastApi
1. Client send request to server
    * Suppose client want to update name in item
    * Client send params for update (id, name, etc...), PEDANTIC SAY WHICH PARAMS NEED
2. Receive request to FastAPI
   * Server(FastAPI) receives request
   * Validate params with pydantic 
   * Return pydantic model to view
3. View
   * can use dependency injection to get session, object, etc. 
   * do view: use crud, services, etc.
   * return response