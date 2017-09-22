#!/usr/bin/python3
'''
We have a video with `NUM_FRAMES` that we want to partition in batches of size `BATCH_SIZE`.
In addition, the batches can have an overlapping number of frames given by `OVERLAP_SIZE`.
'''

NUM_FRAMES = 10000
BATCH_SIZE = 750
OVERLAP_SIZE = 50

assert NUM_FRAMES > 0 and BATCH_SIZE > 0 and OVERLAP_SIZE >= 0
assert NUM_FRAMES > BATCH_SIZE and BATCH_SIZE > OVERLAP_SIZE


def main():
    ''' Generate lists with batch sizes, start and end frames. '''

    start_frames = [
        start_frame
        for start_frame in range(0, NUM_FRAMES, BATCH_SIZE - OVERLAP_SIZE)
    ]
    end_frames = [
        end_frame
        for end_frame in range(BATCH_SIZE, NUM_FRAMES + 1,
                               BATCH_SIZE - OVERLAP_SIZE)
    ]

    if end_frames[-1] != NUM_FRAMES:
        end_frames.append(NUM_FRAMES)

    start_frames = start_frames[0:len(end_frames)]

    batch_sizes = [
        end_frames[i] - start_frames[i] for i in range(0, len(start_frames))
    ]

    return start_frames, end_frames, batch_sizes


if __name__ == "__main__":
    start_frames, end_frames, batch_sizes = main()
