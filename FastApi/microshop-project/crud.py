import asyncio

from sqlalchemy import select, Result, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import db_helper, User, Post, Profile


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print(user)
    return user


async def get_user_by_profile(session: AsyncSession, profile_id: int) -> User | None:
    profile = session.get(Profile, profile_id)
    stmt = select(User).where(User.profile == profile)
    user: User | None = await session.scalar(stmt)
    return user


async def show_users_with_profiles(session: AsyncSession):
    # select - command to db
    # session scalars - get result from query
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    users: ScalarResult = await session.scalars(stmt)
    for user in users:
        print(f"{user!r}")
        print(f"{user.profile!r}, first name: {user.profile.first_name!r}")


async def get_users_with_posts(session: AsyncSession):
    stmt = (
        select(User)
        .options(
            # joinedload(User.posts)
            selectinload(User.posts)
        )
        .order_by(User.id)
    )

    # begin execute the query and get Result
    # before we can do query manipulations like scalars
    res: Result = await session.execute(stmt)
    users = res.scalars()
    for user in users:
        print(user)
        print(user.posts)


async def get_posts_with_authors(session: AsyncSession):
    stmt = select(Post).options(joinedload(Post.user)).order_by(Post.id)
    posts: ScalarResult = await session.scalars(stmt)
    for post in posts:
        print(post)
        print(post.user)


async def get_users_with_posts_and_profiles(session: AsyncSession):
    stmt = (
        select(User)
        .options(selectinload(User.posts), joinedload(User.profile))
        .order_by(User.id)
    )

    users = await session.scalars(stmt)
    for user in users:
        print(user)
        print(user.profile and user.profile.first_name)
        for post in user.posts:
            print(post)


async def get_profiles_with_users_and_users_with_posts(session):
    stmt = (
        select(Profile)
        .join(
            Profile.user
        )  # for manipulations in query with nested data, in this time it is User (filter, etc..)
        .options(
            joinedload(Profile.user).selectinload(User.posts)
        )  # nested join, for load data only for load
        .where(User.id == 1)  # filter, for filter Profile don't use join()
        .order_by(Profile.id)  # ordering
    )

    profiles = await session.scalars(stmt)
    for profile in profiles:
        print(profile.first_name)
        print(profile.user)
        for post in profile.user.posts:
            print(post)


async def create_posts(
    session: AsyncSession, user_id: int, posts_data: list[dict]
) -> list[Post]:
    posts = []
    for post_data in posts_data:
        posts.append(Post(user_id=user_id, **post_data))
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print(user)
    return user


async def create_user_profile(
    session: AsyncSession, user_id: int, **kwargs
) -> Profile | None:
    profile = Profile(user_id=user_id, **kwargs)

    session.add(profile)
    await session.commit()
    return profile


async def main_relations(session: AsyncSession):
    await get_profiles_with_users_and_users_with_posts(session)


async def main():
    async with db_helper.session_factory() as session:  # type: AsyncSession
        # await main_relations(session)
        await demo_m2m()


async def demo_m2m():
    pass


if __name__ == "__main__":
    asyncio.run(main())
