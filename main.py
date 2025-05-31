from rich.console import Console
from rich.traceback import install
import click
import os

# services
from yt_dlp import YoutubeDL


console = Console()
cur_dir = os.getcwd()
install()


# main function

@click.command()
@click.argument('url')
@click.option('-youtube', is_flag=True, help='Download video from youtube')
def main(url, youtube):
    if youtube:
        console.print('[blue]Downloading video...')
        try:
            with YoutubeDL({'format': 'best', 'quiet': True}) as ydl:
                ydl.download(url)
                console.print(f'[green]Video downloaded!\nDestination: {cur_dir}')
        except Exception as e:
            console.print(f'[red]Unknown error: {e}')

if __name__ == "__main__":
    main()