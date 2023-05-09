struct read_data {
	short age;
	char name[10];
};

struct message {
	long msg_type;
	struct read_data data;
};
