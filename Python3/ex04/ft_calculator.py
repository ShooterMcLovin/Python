class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        return sum(v1 * v2 for v1, v2 in zip(V1, V2))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        return list(v1 +  v2 for v1, v2 in zip(V1, V2))
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        return list(v1 -  v2 for v1, v2 in zip(V1, V2))