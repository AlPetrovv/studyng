# SQLAlchemy

## Database

<ul>
    <li>
        DeclarativeBase - Base class for models (like class Model in Django)
    </li>
    <li>
        Mapped[type] - annotation that type is column in db
        Mapped[str | None] - annotation that str | None is column in db
        mapped_column - add params to column in db. ONLY for column(not for type), like primary_key, unique 
        mapped_column - default not null
        <ul> Params for mapped_column: 
            <li> 
                default - use default value when create obj by sqlalchemy
            </li>
            <li>
                server_default - default for postgresql
            </li>
            <li>
                nullable - nullable if not use null like default
            </li>
            <li>
                index - create index in db
            </li>
        </ul>
    </li>
    <li>
        Additional types validation in alchemy (ONLY for types, not column), like max_length
        - String,Text
        - Integer, Decimal
        - Date, Time, DateTime
        - Boolean
        - UUID
        - ForeignKey
        - Etc...
    </li>
    <li>
        relationship - create relationship between models(sqlalchemy)
        <ul> Params for relationship:
            <li>back_populates - create reverse relationship by name</li>
        </ul>
        <ul> Examples: 
            <li>
                user: Mapped["User"] = relationship(back_populates="posts")
            </li>
            <li>
                posts: Mapped[list["Post"]] = relationship(back_populates="user")
            </li>
        </ul>
        ...
    </li>
    <li>
        session: AsyncSession - create session to db <br>
        what is session in db?
        <ul> Params:
            <li>
                execute - 
            </li>
            <li>
                scalars - 
            </li>
            <li>
                scalar_one_or_none and scalar_one
            </li>
        </ul>
    </li>
</ul>

## ORM

<ul>
    <li>
        select - create query to db (Base for almost all commands) <br>
        select like SELECT in SQL Query language <br>
        Examples:
        <ul>
            <li>
                stmt = select(User) - select all users
            </li>
        </ul>
    </li>
    <li>
        where - filter query by smth <br>   
        Examples:
        <ul>
            <li>
                stmt = select(User).where(User.id == 1) - select user with id = 1
            </li>
        </ul>
    </li>
    <li> 
        order_by - order query by smth <br>
        Examples:
        <ul>
            <li>
                stmt = select(User).order_by(User.id) - select all users order by id
            </li>
        </ul>
    </li>
    <li>
        options - add options to query (like join, eagerload, additional query, etc...)<br>
        <ul> Params for options:
            <li>
                joinedload - add join to query, usually use for OneToOne <br>
                Examples:
                    <ul>
                        <li>
                            stmt = select(User).options(joinedload(User.posts)) - select all users with posts by join
                        </li>
                    </ul>
            </li>
            <li>
                selectinload - add eagerload to query (additional query), usually use for ManyToOne or OneToMany <br>
                Examples:
                    <ul>
                        <li>
                            stmt = select(User).options(selectinload(User.posts)) - select all users with posts by 2 queries
                        </li>
                    </ul>
            </li>
            <li>    
                nested join - combination selectinload and joinedload ( after in text "s and l") <br>
                If we use "s or l"and want to add connected data, we call object that called in "s or l" <br>
                Examples:
                <ul>
                    <li>
                        stmt = select(Profile).options(joinedload(Profile.user).selectinload(User.posts))
                    </li>
                </ul>
            </li>
        </ul>
    </li>
</ul>

