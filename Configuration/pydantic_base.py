from typing import List, Optional

import pydantic


# Define errors
class Feature_Target(Exception):
    """Custom error"""
    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class Config_file(pydantic.BaseModel):
    """To be read from config files"""
    data_path: str
    features: List[str]
    target: List[str]
    model_save: str
    train_retrain: str
    max_epochs: str
    sequence: bool
    test_size: Optional[str]
    val_size: Optional[str]
    print_logs: bool


    @pydantic.validator("target")
    @classmethod
    def target_valid(cls, value) -> None:
        for element in value:
            if element in Config_file.features:
                raise Feature_Target(value=value, message="Target is in Features")
        return value

    class Config:
        """Pydantic config class"""
        allow_mutation = False
        anystr_lower = True
