
from pydantic import BaseModel,Field
from typing import Literal, List, Union

class RentalPricePredictInput(BaseModel):
    model_key:str
    mileage: int = Field(ge=0,description="Mileage must be non-negative")
    engine_power: int = Field(ge=0, description="Engine power must be non-negative")
    fuel: Literal["diesel", "petrol", "electro", "hybrid_petrol"]
    paint_color: Literal["green","silver","blue","grey","brown","black","red","beige","white","orange"]
    car_type:Literal["subcompact","estate","hatchback","van","sedan","convertible","suv","coupe"]
    private_parking_available:bool
    has_gps:bool	
    has_air_conditioning:bool	
    automatic_car:bool	
    has_getaround_connect:bool	
    has_speed_regulator:bool
    winter_tires:bool