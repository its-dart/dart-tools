from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_dartboard_layout import UserDartboardLayout


T = TypeVar("T", bound="PaginatedUserDartboardLayoutList")


@_attrs_define
class PaginatedUserDartboardLayoutList:
    """
    Attributes:
        count (Union[Unset, int]):  Example: 123.
        next_ (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=400&limit=100.
        previous (Union[Unset, None, str]):  Example: http://api.example.org/accounts/?offset=200&limit=100.
        results (Union[Unset, List['UserDartboardLayout']]):
    """

    count: Union[Unset, int] = UNSET
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[Unset, List["UserDartboardLayout"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_dartboard_layout import UserDartboardLayout

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = UserDartboardLayout.from_dict(results_item_data)

            results.append(results_item)

        paginated_user_dartboard_layout_list = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_user_dartboard_layout_list.additional_properties = d
        return paginated_user_dartboard_layout_list

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
