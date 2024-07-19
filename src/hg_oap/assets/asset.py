from dataclasses import dataclass

from hg_oap.units import Quantity
from hg_oap.units.unit import Unit
from hg_oap.units.unit_system import UnitConversionContext
from hg_oap.utils.exprclass import ExprClass
from hgraph import CompoundScalar


@dataclass(frozen=True)
class Asset(CompoundScalar, ExprClass, UnitConversionContext):
    """
    A thing of value that can be held.
    Assets are not instruments (i.e. cannot be traded directly), but can be used in instruments as underlyers.
    """

    symbol: str


@dataclass(frozen=True)
class PhysicalAsset(Asset):
    """
    A tangible thing, for example: raw materials, infrastructure, equipment, etc.

    The physical asset has a default unit - for example, copper is often measured in metric tonnes, electricity in
    MWh.  The contract size could be measured in a different unit - for example, electricity could be priced as MW
    over a period rather than a fixed quantity of MWh.

    The actual traded unit can also vary according to the contract - copper could be traded in pounds as well as tonnes.
    The unit conversion factors can be used to convert between units of different dimensions.
    """

    name: str
    default_unit: Unit = None  # TODO - add a Unit.null?
    unit_conversion_factors: tuple[Quantity[float], ...] = ()


@dataclass(frozen=True)
class FinancialAsset(Asset):
    """
    A financial asset is a non-tangible asset. Examples include cash, cash equivalents, stocks and bonds.
    """
