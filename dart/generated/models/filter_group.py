from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_connector import FilterConnector

if TYPE_CHECKING:
    from ..models.filter_assignee import FilterAssignee
    from ..models.filter_search import FilterSearch
    from ..models.filter_set import FilterSet


T = TypeVar("T", bound="FilterGroup")


@_attrs_define
class FilterGroup:
    """
    Attributes:
        filters (Union['FilterAssignee', 'FilterSearch', 'FilterSet']):
        connector (FilterConnector): * `or` - OR
            * `and` - AND
    """

    filters: Union["FilterAssignee", "FilterSearch", "FilterSet"]
    connector: FilterConnector
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.filter_assignee import FilterAssignee
        from ..models.filter_set import FilterSet

        filters: Dict[str, Any]

        if isinstance(self.filters, FilterAssignee):
            filters = self.filters.to_dict()

        elif isinstance(self.filters, FilterSet):
            filters = self.filters.to_dict()

        else:
            filters = self.filters.to_dict()

        connector = self.connector.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "connector": connector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_assignee import FilterAssignee
        from ..models.filter_search import FilterSearch
        from ..models.filter_set import FilterSet

        d = src_dict.copy()

        def _parse_filters(data: object) -> Union["FilterAssignee", "FilterSearch", "FilterSet"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_type_0 = FilterAssignee.from_dict(data)

                return componentsschemas_filter_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_type_1 = FilterSet.from_dict(data)

                return componentsschemas_filter_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_type_2 = FilterSearch.from_dict(data)

            return componentsschemas_filter_type_2

        filters = _parse_filters(d.pop("filters"))

        connector = FilterConnector(d.pop("connector"))

        filter_group = cls(
            filters=filters,
            connector=connector,
        )

        filter_group.additional_properties = d
        return filter_group

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
