#Really just a copy of the systemtap rickrolling script,found on github.com.
probe kernel.function("do_filp_open") {
	p = kernel_string($pathname);
	l = strlen(p);
	if (substr(p,l-4,l) == ".mp3")
	{
		$pathname = %{ (long) "/home/anand/Music/Bob Dylan - The Very Best Of Bob Dylan (2000) 320 vtwin88cube/Disc\ 1/01." %};
	}
}
