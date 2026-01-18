import collections.abc
import typing

__all__ = ["merge", "merge_with"]

@typing.overload
def merge_with[K, V]() -> typing.Callable[
    ..., dict[K, V] | collections.abc.MutableMapping[K, V]
]: ...
@typing.overload
def merge_with[K, V](
    func: typing.Callable[[list[V]], V], /
) -> typing.Callable[..., dict[K, V] | collections.abc.MutableMapping[K, V]]: ...
@typing.overload
def merge_with[K, V](
    func: typing.Callable[[list[V]], V],
    d: collections.abc.Mapping[K, V],
    /,
) -> dict[K, V]: ...
@typing.overload
def merge_with[K, V](
    func: typing.Callable[[list[V]], V],
    d: collections.abc.Mapping[K, V],
    d2: collections.abc.Mapping[K, V],
    /,
    *dicts: collections.abc.Mapping[K, V],
) -> dict[K, V]: ...
@typing.overload
def merge_with[K, V](
    func: typing.Callable[[list[V]], V],
    d: collections.abc.Mapping[K, V],
    d2: collections.abc.Mapping[K, V],
    /,
    *dicts: collections.abc.Mapping[K, V],
    factory: typing.Callable[[], collections.abc.MutableMapping[K, V]],
) -> collections.abc.MutableMapping[K, V]: ...
@typing.overload
def merge_with[K, V](
    func: typing.Callable[[list[V]], V],
    /,
    *,
    factory: typing.Callable[[], collections.abc.MutableMapping[K, V]],
) -> typing.Callable[..., collections.abc.MutableMapping[K, V]]: ...
@typing.overload
def merge[K, V]() -> typing.Callable[
    ..., dict[K, V] | collections.abc.MutableMapping[K, V]
]: ...
@typing.overload
def merge[K, V](d: collections.abc.Mapping[K, V], /) -> dict[K, V]: ...
@typing.overload
def merge[K, V](
    d: collections.abc.Mapping[K, V],
    d2: collections.abc.Mapping[K, V],
    /,
    *dicts: collections.abc.Mapping[K, V],
) -> dict[K, V]: ...
@typing.overload
def merge[K, V](
    d: collections.abc.Mapping[K, V],
    d2: collections.abc.Mapping[K, V],
    /,
    *dicts: collections.abc.Mapping[K, V],
    factory: typing.Callable[[], collections.abc.MutableMapping[K, V]],
) -> collections.abc.MutableMapping[K, V]: ...
@typing.overload
def merge[K, V](
    *,
    factory: typing.Callable[[], collections.abc.MutableMapping[K, V]],
) -> typing.Callable[..., collections.abc.MutableMapping[K, V]]: ...
