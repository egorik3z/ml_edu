import json
import os

def remove_solutions(input_filepath, output_filepath):
    new_cells = []
    
    with open(input_filepath) as f:
        data = json.load(f)

    cell_list = data['cells']
    
    for cell in cell_list:
        if cell['cell_type'] == 'code':
            cell['outputs'] = []
            
            skip_cell = False
            source_data = cell['source']
            for source_line in source_data:
                if 'SOLUTION' in source_line:
                    skip_cell=True
                    break
                
                if 'DEBUG' in source_line:
                    skip_cell=True
                    break
                
            if skip_cell:
                continue
    
        new_cells.append(cell)
    
    data['cells'] = new_cells
    
    with open(output_filepath, 'w') as f:
        json.dump(data, f)
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('directory', metavar='directory', type=str,
                        help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
                        # const=sum, default=max,
                        # help='sum the integers (default: find the max)')

    args = vars(parser.parse_args())

    root_dirpath = args['directory']
    out_dirpath = 'notebooks'
    in_fnames = [fname for fname in os.listdir(root_dirpath) if fname.endswith('.ipynb')]
    
    in_fpaths = [os.path.join(root_dirpath, fname) for fname in in_fnames]
    out_fpaths = [os.path.join(out_dirpath, fname) for fname in in_fnames]

    for in_fpath, out_fpath in zip(in_fpaths, out_fpaths):
        print(f'Processing {in_fpath}')
        remove_solutions(in_fpath, out_fpath)
