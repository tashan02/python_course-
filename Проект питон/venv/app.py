import flask
from data_processing import exp_run_average_adaptive, kalman, median, one_sample, read_csv, run_middle, stret_sample
import matplotlib.pyplot as plt


app = flask.Flask('Проект по питону', static_folder= 'static')

def draw_graph(filename:str, data, data2):
    plt.switch_backend('agg')
    plt.plot(data)
    if data2:
        plt.plot(data2)
    image_filename = f'/static/temp/images/{filename}.png'
    plt.savefig(f'.{image_filename}')
    return flask.render_template("index.html", image_filename=image_filename)

@app.get('/<filename>/')
def simple_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    return draw_graph(f'{filename}_simple', data)

@app.get('/<filename>/one_sample')
def one_sample_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = one_sample()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_one_sample', data, data2)

@app.get('/<filename>/stret_sample')
def stret_sample_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = stret_sample()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_stret_sample', data, data2)

@app.get('/<filename>/run_middle')
def run_middle_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = run_middle()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_run_middle', data, data2)

@app.get('/<filename>/exp_run_average_adaptive')
def exp_run_average_adaptive_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = exp_run_average_adaptive()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_exp_run_average_adaptive', data, data2)

@app.get('/<filename>/median')
def median_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = median()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_median', data, data2)

@app.get('/<filename>/kalman')
def kalman_graph(filename:str):
    data = read_csv(f'./data/{filename}.txt')
    calc = kalman()
    data2 = [calc(x) for x in data]
    return draw_graph(f'{filename}_kalman', data, data2)



if __name__=='__main__':
    app.run('0.0.0.0', port = 9979, debug = True)