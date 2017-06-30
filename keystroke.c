#include <fcntl.h>
#include <ioctl.h>
#include <unistd.h>
#include <linux/input.h>
#include <linux/uinput.h>

/* Set up a fake keyboard device */
fd = open("/dev/uinput", O_WRONLY | O_NONBLOCK); // or /dev/input/uinput
ioctl(fd, UI_SET_EVBIT, EV_KEY);
struct uinput_user_dev uidev = …;
write(fd, &uidev, sizeof(uidev));
ioctl(fd, UI_DEV_CREATE);

/* Send an event */
struct input_event ev;
memset(&ev, 0, sizeof(ev));
ev.type = EV_KEY;
ev.code = KEY_P;
ev.value = 1;
write(fd, &ev, sizeof(ev));

struct input_event ev;
memset(&ev, 0, sizeof(ev));
ev.type = EV_KEY;
ev.code = KEY_P;
ev.value = 0;
write(fd, &ev, sizeof(ev));

/* Clean up */
ioctl(fd, UI_DEV_DESTROY);
close(fd);
