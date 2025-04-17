import asyncio
from collections.abc import AsyncGenerator

from sqlalchemy import select, Result, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import OrderItemAssociation
from core.models import db_helper, User, Post, Profile, Order, Item


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


async def create_order(
    session: AsyncSession,
    promocode: str | None = None,
) -> Order:
    order = Order(promocode=promocode)
    session.add(order)
    await session.commit()
    print(order)
    return order


async def create_item(
    session: AsyncSession,
    name: str,
    description: str,
    price: int,
) -> Item:
    item = Item(
        name=name,
        description=description,
        price=price,
    )
    session.add(item)
    await session.commit()
    print(item)
    return item


async def get_order_by_id(session: AsyncSession, order_id: int) -> Order:
    order = await session.scalar(
        select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
    )
    return order


async def add_items_to_order(
    order: int | Order,
    items: list[Item],
):
    if isinstance(order, int):
        order = (
            select(Order).options(selectinload(Order.items)).where(Order.id == order)
        )

    order.items.extend(items)


async def create_order_with_items(session: AsyncSession):
    order1 = await create_order(session, "code1")
    order2 = await create_order(session, "code2")
    order3 = await create_order(session)

    item1 = await create_item(session, name="Bread", description="Food", price=10)
    item2 = await create_item(session, name="Soup", description="Alchemy", price=30)
    item3 = await create_item(session, name="Mouse", description="PC", price=100)

    order1 = await get_order_by_id(session, order_id=order1.id)
    order2 = await get_order_by_id(session, order_id=order2.id)
    order3 = await get_order_by_id(session, order_id=order3.id)

    await add_items_to_order(order=order1, items=[item1, item2])
    await add_items_to_order(order=order2, items=[item2])
    await add_items_to_order(order=order3, items=[item3, item1, item2])

    await session.commit()


async def get_orders_with_items(session: AsyncSession) -> AsyncGenerator:
    """
    function that yield orders with items (m2m relation)
    """
    stmt = select(Order).options(selectinload(Order.items)).order_by(Order.id)
    orders: ScalarResult[Order] = await session.scalars(stmt)
    for order in orders:  # type: Order
        yield order


async def get_orders_with_items_with_assoc(session: AsyncSession) -> AsyncGenerator:
    smtm = (
        select(Order)
        .options(
            selectinload(Order.items_details).joinedload(OrderItemAssociation.item),
        )
        .order_by(Order.id)
    )
    orders = await session.scalars(smtm)

    for order in orders:
        yield order


async def demo_m2m(session: AsyncSession):
    """
    demo examples m2m relation
    """
    # async for order in get_orders_with_items_with_assoc(session):  # type: Order
    #     print("".center(50, "*"))
    #     print(f" Order id:{order.id}, Order created at:{order.created_at}")
    #     print("Items:")
    #     for item_details in order.items_details:  # type: OrderItemAssociation
    #         print(
    #             f"Item id: {item_details.id},  Item name: {item_details.item.name}, Item price: {item_details.item.price}"
    #         )


async def create_gift_items_for_exists_order(session: AsyncSession):
    orders = get_orders_with_items_with_assoc(session=session)

    gift_item = await create_item(
        session,
        name="Gift",
        description="Gift",
        price=0,
    )

    async for order in orders:
        print("".center(50, "*"))
        order.items_details.append(
            OrderItemAssociation(count=1, unit_price=10, item=gift_item)
        )

    await session.commit()


async def main():
    async with db_helper.session_factory() as session:  # type: AsyncSession
        # await main_relations(session)
        await demo_m2m(session)


if __name__ == "__main__":
    asyncio.run(main())
