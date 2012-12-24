
extern id_ip_map *id_ip_table;

struct id_ip_map
{
    char *chat_id;
    char *ip_port_str;
};

struct message
{
    char *mesg;
       
};


int register_id(id,ip,port)
{
    *(id_ip_table+1).chat_id = id;

    *(id_ip_table+1).ip_port_str= ip+port;
    return 1;
}

int initialize_table(int nchat)
{
    return memset(id_ip_table,0,sizeof(struct id_ip_map));
    

}


int send_message(message * msg)
{
    return 1;
}


int recv_message()
