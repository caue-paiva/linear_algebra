from functools import reduce

def read_vecs(vec_num:int)->list[list[int]]:
   vec_list:list[list[int]] = []

   for i in range(vec_num):
      line_elements:list[str] = input().split(" ")
      vector:list[int] = list(map(int,line_elements))
      vec_list.append(vector)
   
   return vec_list

def binary_vals_of_canonic_base(dimension:int)->set[int]:
   """
   Dado a dimensão dos vetores, gera os valores binários que eles representam.
   Ex R3:
   (1,0,0) => 1
   (0,1,0) => 2
   (0,0,1) => 4
   Retorno set([1,2,4])

   Args:
      dimension(int): dimensao dos vetores

   Return:
      (set[int]): conjuntos com os valores inteiro que representam os vetores da base canônica
   """
   return set([2**x for x in range(dimension)])

def reduce_vec_list(accumulator:int,vec_tuple:tuple[int,int])->int:
   """
   função para ser usada na função reduce() para reduzir um vetor a um escalar
   """
   vec_element_index:int = vec_tuple[0] #index do elemento no vetor
   vec_element:int = vec_tuple[1] #elemento do vetor

   if vec_element != 0: #elemento não é zero
      return accumulator + 2**vec_element_index
   
   return accumulator #elemento é zero

def reduce_all_vectors(vectors:list[list[int]])->set[int]:
   """
   Reduz cada vetor a sua represetação binaria (contando que cada elemento não 0 conta como um 1 binário, 
   pois estamos buscando a base canônica ou multiplos dela)
   Ex R3:
   (2,2,0) == (1,1,0) => 3
   (3,0,1) == (1,0,1) => 5

   É usada a função reduce da stdlib, que recebe um iterável e reduz ele a um escalar, nesse caso a representação binaria
   
   Args:
      vectors(list[list[int]]): lista de vetores
   
   Return:
      (set[int]): conjunto de valores dos vetores reduzidos
   """
   reduce_vec_to_int = lambda x: reduce( #dado um vetor x (list[int]) reduz ele pra um inteiro
      reduce_vec_list,  #função para reduzir vetor a um escalar pela soma de seus elementos não 0
      enumerate(x), #enumera a lista x (vetor) em um tupla cujo primeiro elemento é o index e o segundo é o valor 
      0 #valor inicial do accumulador do reduce
   )
   return set(map(reduce_vec_to_int,vectors))

def main()->None:
   """
   Esse código usa a lógica de mapear vetores para uma representação binário, contando com valores podendo ser 0 ou outro número (mapeado para 1, pois é um múltiplo)
   """
   first_line:str = input() #le valores de dimensao e num de vetores
   numbers:list[int] = list(map(int,first_line.split(" ")))
   
   DIMENSION:int = numbers[0] #constantes
   VEC_NUM:int = numbers[1]

   vecs:list[list[int]] = read_vecs(VEC_NUM) #le os vetores
   
   canonical_base_vecs:set[int] = binary_vals_of_canonic_base(DIMENSION) #acha os valores representantes dos vetores da base canônica
   reduced_vecs:set[int] = reduce_all_vectors(vecs) #acha os valores representantes dos vetores de input
   
   is_base_of:bool = canonical_base_vecs.issubset(reduced_vecs) #os vetores da base canônica estão contidos nos vetores de input?
   if is_base_of:
      print("SimTia")
   else:
      print("Não")



if __name__ == "__main__":
   main()
