(defn mid-point [p1 p2]
  (map #(/ (+ % %2) 2) p1 p2))

(defn next-triangles [[top left right]]
  [[top (mid-point top left) (mid-point top right)]
   [(mid-point left top) left (mid-point left right)]
   [(mid-point right top) (mid-point left right) right]])

(def canvas (js/document.getElementById "render"))
(doto (.getContext canvas "2d")
  (aset "strokeStyle" "black")
  (.clearRect 0 0 (.-width canvas) (.-height canvas)))

(defn draw-triangle [canvas [[x1 y1] [x2 y2] [x3 y3]]]
  (doto (.getContext canvas "2d")
    (.beginPath)
    (.moveTo x1 y1)
    (.lineTo x2 y2)
    (.lineTo x3 y3)
    (.lineTo x1 y1)
    (.stroke)
    (.closePath)))

(defn draw-sierp [canvas initial n]
  (when (> n 0)
    (doseq [triangle (next-triangles initial)]
      (draw-triangle canvas triangle)
      (draw-sierp canvas triangle (dec n)))))

(draw-sierp canvas [[0 500] [250 0] [500 500]] 6)
