(defproject collatz "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [com.taoensso/timbre "4.7.4"]
                 [criterium "0.4.4"]
                 ]
  :profiles {:uberjar {:aot :all}}
  :main ^:skip-aot collatz.core
  )
