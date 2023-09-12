import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.batch import Batch

T = TypeVar("T", bound="YcIntegration")


@_attrs_define
class YcIntegration:
    """
    Attributes:
        batch (Batch): * `S05` - S05
            * `W06` - W06
            * `S06` - S06
            * `W07` - W07
            * `S07` - S07
            * `W08` - W08
            * `S08` - S08
            * `W09` - W09
            * `S09` - S09
            * `W10` - W10
            * `S10` - S10
            * `W11` - W11
            * `S11` - S11
            * `W12` - W12
            * `S12` - S12
            * `W13` - W13
            * `S13` - S13
            * `W14` - W14
            * `S14` - S14
            * `W15` - W15
            * `S15` - S15
            * `W16` - W16
            * `S16` - S16
            * `IK12` - IK12
            * `W17` - W17
            * `S17` - S17
            * `W18` - W18
            * `S18` - S18
            * `W19` - W19
            * `S19` - S19
            * `W20` - W20
            * `S20` - S20
            * `W21` - W21
            * `S21` - S21
            * `W22` - W22
            * `S22` - S22
            * `W23` - W23
        batch_full_name (str):
        demo_day_date_str (Optional[datetime.date]):
    """

    batch: Batch
    batch_full_name: str
    demo_day_date_str: Optional[datetime.date]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch = self.batch.value

        batch_full_name = self.batch_full_name
        demo_day_date_str = self.demo_day_date_str.isoformat() if self.demo_day_date_str else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch": batch,
                "batchFullName": batch_full_name,
                "demoDayDateStr": demo_day_date_str,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch = Batch(d.pop("batch"))

        batch_full_name = d.pop("batchFullName")

        _demo_day_date_str = d.pop("demoDayDateStr")
        demo_day_date_str: Optional[datetime.date]
        if _demo_day_date_str is None:
            demo_day_date_str = None
        else:
            demo_day_date_str = isoparse(_demo_day_date_str).date()

        yc_integration = cls(
            batch=batch,
            batch_full_name=batch_full_name,
            demo_day_date_str=demo_day_date_str,
        )

        yc_integration.additional_properties = d
        return yc_integration

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
