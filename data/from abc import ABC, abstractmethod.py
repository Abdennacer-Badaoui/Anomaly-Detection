from abc import ABC, abstractmethod
from cv2 import exp
import matplotlib.pyplot as plt
import random
from typing import Any, List, Optional, Tuple, Union
import torch

training_data = torch.load('C:/Users/PPiC/Desktop/training_data_points.pt')

class ActivationFunction(ABC):
    
    @abstractmethod
    def compute(self):
        pass
    
    @abstractmethod
    def differentiate(self):
        pass

    
class CostFunction(ABC):
    
    @abstractmethod
    def compute(self):
        pass
    
    @abstractmethod
    def differentiate(self):
        pass

class Sigmoid(ActivationFunction):
    
    @classmethod
    def compute(cls, z: torch.Tensor) -> torch.Tensor:
        return (1+exp(-z))**(-1)

    @classmethod
    def differentiate(cls, z: torch.Tensor) -> torch.Tensor:
        return Sigmoid.compute(cls, z)*(1-Sigmoid.compute(cls, z))