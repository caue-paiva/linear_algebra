from abc import ABC, abstractmethod
from typing import Type
from copy import copy

class VectorSpace(ABC):
   
   @abstractmethod
   def __validate_values(self,values:list[float])->bool:
      """
      Valida se os elementos do vetor respeitam uma regra do espaço vetorial
      """
      pass

   @abstractmethod
   def vector_adition(self,vector:Type["VectorSpace"])->Type["VectorSpace"]:
      pass


   @abstractmethod
   def scalar_multi(self,scalar:int|float)->Type["VectorSpace"]:
      pass


class StandardVecSpace(VectorSpace):
   __values:list[float]
   dimension:int

   def __init__(self,vals:list[float])-> None:
      if not self.__validate_values:
         raise RuntimeError("Valores de input não fazem parte desse espaço vetorial")
      
      list_len:int = len(vals)
      if list_len < 2:
         raise RuntimeError("Numéro de dimensões mínimas é 2")
      if not isinstance(vals,list):
         raise RuntimeError("Argumento vals deve ser uma lista")
      
      self.__values = copy(vals)
      self.dimension = len(vals)

   def get_values(self)->list[float]:
      return self.__values

   def __validate_values(self, values: list[float]) -> bool:
      return all(map(lambda x: isinstance(x,float),values))
   
   def vector_adition(self, vector:"StandardVecSpace" )->"StandardVecSpace":
      if vector.dimension != self.dimension:
         raise RuntimeError("Vetores devem ter a mesma dimensão")
      
      new_vals:list[float]  = list(map(lambda x,y: x+y, self.__values, vector.get_values()))
      return StandardVecSpace(new_vals)   

   def scalar_multi(self, scalar: int | float) -> "StandardVecSpace":
      new_vals:list[float]  = list(map(lambda x: x*scalar,self.__values))
      return StandardVecSpace(new_vals)


