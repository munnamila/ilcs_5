import frame2video
import video2frame

if __name__ == '__main__':
    video2frame.video2frame('/Users/songminglun/Downloads/kurita_001.mp4', '/Users/songminglun/Downloads/kurita')
    frame2video.frmae2video('/Users/songminglun/Downloads/kurita', (1280, 720))