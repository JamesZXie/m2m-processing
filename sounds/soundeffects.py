import pyaudio
import wave


def play_sound(track):
    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(track, "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()


def get_wav_file():
    not_done = True

    file = open('sfx.txt', 'r')
    all_tracks = file.read()
    available_tracks = []

    for track in all_tracks.split():
        available_tracks.append(track)

    while not_done:
        print("Input track to play\n"
              "Type 'ls' to list all available tracks\n"
              "Press 'q' to quit\n")
        requested_track = input()

        if requested_track == 'ls':
            print("\nAvailable tracks\n"
                  "-----------------")
            for track in available_tracks:
                print(track)
            print()

        elif requested_track == 'q':
            print("Goodbye")
            not_done = False

        elif requested_track in available_tracks:
            for track in available_tracks:
                if requested_track == track:
                    print("Playing " + track + '\n')
                    wav_file = track + ".wav"
                    play_sound(wav_file)
                    break

        else:
            print("Invalid input\n"
                  "Try again\n\n")


if __name__ == '__main__':
    get_wav_file()
