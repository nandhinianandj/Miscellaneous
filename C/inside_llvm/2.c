define i32 @foo(i32 %aa, i32 %bb,i32 %cc) nounwind {
entry:
  %add = add nsw i32 %aa, %bb
  %div = sdiv i32 %add, %cc
  ret i32 %div
}
