import math
def buscaSolucao(f,a,b,N):
    '''Aproxima a solução da equação f(x)=0 no intervalo [a,b] pelo método da BISSEÇÂO.
       Quem fizer cálculo numérico verá esse método!

    Parâmetros
    ----------
    f : A função f(x)        
    a,b : Números reais representando o ínicio e o fim do intervalo [a,b].
        O intervalo de busca da solução
        Caso f(a)*f(b) >= 0 o programa retorna falso, pois a solução não
        é garantida nesse caso.
    N : Um inteiro maior do que ZERO.
        Número finito de iterações (estamos em precisão finita!).

    Returns
    -------
    x_N : Número Real
        ponto central do intervalo N calculado pelo algorítmo da bisseção.
        Por exemplo, no primeiro intervalo x_N = (a+b)/2.
    '''
    
    if f(a)*f(b) >= 0:
        print("O método da bisseção falhou! Tente escolher outro intervalo...")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2 #ponto médio
        f_m_n = f(m_n) #avalia a função no ponto médio m_n
        if f(a_n)*f_m_n < 0: #Então a solução deve estar no intervalo [a, m_n]
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0: #Então a solução deve estar no intervalo [m_n, b]
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0: #Então o ponto central m_n é uma raiz de f(x)=0.
            print("Encontrada a solução exata!!")
            return m_n
        else:
            print("O método da bisseção falhou!")
            return None
    return (a_n + b_n)/2 #retorna o valor do ponto m_n
    
    
    '''Exemplos de Uso:
    f = lambda x: x**2 - 2*x -5
    approx_p = buscaSolucao(f,-2,2,100)
    print(approx_p)        
    
    f2 = lambda x: x**7 - 3*x**3+x**2 -1
    approx_p = buscaSolucao(f2,-20,2,100)
    print(approx_p) 
    
    f3 = lambda x: math.cos(x)
    approx_p = buscaSolucao(f,-2,2,100)
    print(approx_p) 
    '''  
