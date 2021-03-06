#include <unistd.h>
#include <sys/syscall.h>
#include <linux/perf_event.h>

int main(void)
{
    struct perf_event_attr attr = {
        .type = PERF_TYPE_SOFTWARE,
        .size = sizeof(struct perf_event_attr),
        .config = 0x00000000ffffffff,
    };

    syscall(__NR_perf_event_open, &attr, getpid(), -1, -1, 0);
    return 0;
}
