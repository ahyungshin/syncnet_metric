# pre-process
# ffmpeg -i video.mp4 -s 224x224 -max_muxing_queue_size 1024 resize.mp4 # resize to 224
# ffmpeg -i resize.mp4 -filter:v "crop=160:160:30:90" -c:a copy crop.mp4 # crop face (we have to control)
# ffmpeg -i crop.mp4 -s 224x224 -max_muxing_queue_size 1024 resize.mp4 # resize to 224
# ffmpeg -i resize.mp4 -i macron_gt.wav -c:v copy -c:a aac video_preprocess.mp4 # combine with audio (if there is no audio)

python -u syncnet_metric.py --input-path 'example.avi'