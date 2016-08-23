(ns collatz.core
  (require [taoensso.timbre.profiling :as profiling])
  (use criterium.core)
  );:require [clojure2minizinc.core :as mz])
; -- program to a, find decidability of a collatz seq.
; --            b, find length of a collatz seq
; --        given: an integer

; -- Insights/key shortcuts:
;               a, each of the element in a sequence will have had it's collatz seq length already
;calculated
;               b, Any number that is a power of 2 will have seq. length of power + 1. for ex: 2^2 = 4
;will have seq length 3.  So once we hit a 2^n form we can stop and find log 2 + 1, instead of
;generating sequence
(defn power_of_2 [n] (and (not= n 0) (== (bit-and n (- n 1) ) 0) ) )
(defn next-collatz [n]
  (profiling/p :next-collatz
     (if (even? n) (bit-shift-right n 1) (+ (* 3 n) 1))))

(defn collatz-seq [n]
  (profiling/p :collatz-seq
    (take-while #(not= 1 %) (iterate next-collatz n))))

(defn max-collatz [[na la] [nb lb]]
  (if (> la lb) [na la] [nb lb]))

(defn longest-collatz [start end]
  (reduce max-collatz
      (map #(let [s (collatz-seq %)] [(first s) (inc (count s))])
          (range start (inc end)))))

(defn collatz_length [[n _]]
                   ( println n)
                   (if (== n 1) 1)
                    (if (and (not= n 1)(== (mod n 2) 0)) (+ 1 (collatz_length [(/ n 2)]))
                      ;(if (power_of_2 n) (+ 1 mz/log(n,2)) (+ 1 (collatz_length[(/ n 2)])))
                      )
                   (if (and (not= n 1) (not= (mod n 2) 0)) (+ 1 (collatz_length [(+ 1 (* 3 n ))] ))
               )
)

(defn -main [& args] (collatz_length [5] ))

(profiling/profile :info :Arithmetic (time (longest-collatz  5000 9999)))
(with-progress-reporting (bench (longest-collatz 5000 9999) :verbose))

