@template: post.html
@title: Locgical Scenario Matching from Video
@date: 6-May-2020
@tags: big-data spark scala

# Logical Scenario Matching from Video [Draft]:

Give a short introduction about what a logical scenario is.

- YOLO can detect car/truck/...
- Lane lines can be detected with OpenCV (maybe YOLO also? other CNN?)
- Can we assign absolute lane_id for objects? for ego vehicle?
-- If so, we can label atomic states for moving objects and do the logical scenario matching
- Even this is not possible, still some info can be extracted from video. 
--- Lane changes?
--- How many objects?
--- Object type validation

Optional:
- Run YOLO (OpenCV or TF, or whatever) with Spark on cluster and process videos

Actions:
1. Install OpenCV on Linux vm
2. Install/test darknet-yolo python bindings for single frames
3. Process a session video with darknet-yolo
4. Detect lane lines
5. Combine objects and lane lines

- Run OpenCV with Scala

