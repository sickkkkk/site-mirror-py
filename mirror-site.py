import argparse
from pywebcopy import save_website as saver

def mirror_site(site_url, root_path, folder_name):
    try:
        saver(
            url=site_url,
            project_folder=root_path,
            project_name=folder_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=True,
            delay=None,
            threaded=False,
        )
        return True
    except Exception as e: 
        print(e)
        return False


def main():
    parser=argparse.ArgumentParser(description='A small wrapper around pywebcopy library. \
    Use --help switch for help',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--uri', required=True, type=str, help='HTTPS or HTTP endpoint to grab a site from')
    parser.add_argument('--folder', required=True, type=str, help='Path to folder to save result')
    parser.add_argument('--project', required=True, type=str, help='Path to sub-folder in root folder to save result')
    args=parser.parse_args()
    config=vars(args)

    # Get script working values from config[]
    site_uri=config['uri']
    project_root=config['folder']
    project_dir=config['project']

    if mirror_site(site_uri,project_root,project_dir):
        print(f'Saved {site_uri} to {project_root}/{project_dir}')
    else:
        print(f'Failed to save {site_uri}')


if __name__ == '__main__':
    main()