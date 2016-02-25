template<typename T> static inline T log1p(T x) throw() {
      volatile T y = 1 + x, z = y - 1;
          return z == 0 ? x : x * std::log(y) / z;
}
