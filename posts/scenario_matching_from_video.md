@template: post.html
@title: Scenario Matching from Video
@date: 28-04-2020
@tags: big-data spark scala

# YOLO Scenario Matching from Video:

- Have video footage for 4 views: left, right, front, back
- YOLO can detect car/truck/...
- Lane lines can be detected with OpenCV (maybe YOLO also? other CNN?)
- Can we assign absolute lane_id for objects? for ego vehicle?
-- If so, we can label atomic states for moving objects and do the logical scenario matching
- Even this is not possible, still some info can be extracted from video. 
--- Lane changes?
--- How many objects?
--- Object type validation

- Run YOLO (OpenCV or TF, or whatever) with Spark on cluster and process videos

Actions:
1. Install OpenCV on Linux vm
2. Install/test darknet-yolo python bindings for single frames
3. Process a session video with darknet-yolo
4. Detect lane lines
5. Combine objects and lane lines

- Run OpenCV with Scala

