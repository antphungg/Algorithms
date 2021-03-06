from Animations import runMSTs, runSearchAlgorithms, runCP
import sys

if __name__ == '__main__':
    """
        Argument from command line: `python main.py <input_file_path> <algorithm> <time_delay>(optional)`
        MST algorithms must be one of ['prim', 'kruskal', 'connected_components']
    """
    # if (len(sys.argv)<3) or (len(sys.argv)>5):
    #     raise Exception("Wrong input!!!")
    # input = str(sys.argv[1])
    # al = str(sys.argv[2])
    # if (len(sys.argv)==4):
    #     time_delay = int(sys.argv[4])
    # else: time_delay=500
    
    # if al in ['bfs', 'dfs', 'ucs']:
    #     runSearchAlgorithms(input, al, time_delay)
        
    # elif al in ['prim', 'kruskal']:  
    #     runMSTs(input, al, time_delay)
        
    # elif al in ['connected_components']:
    #     runCP(input, al, time_delay)
    input = 'input.txt'
    time_delay=500
    al = 'dfs'
    runSearchAlgorithms(input, al, time_delay)