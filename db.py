import sqlite3
conn=sqlite3.connect('database.db')
with conn:
    cmd = conn.cursor()
    cmd.execute('''
    create table stock_analysis(
    stock_code varchar(20) not null primary key,
    open_p decimal(20,2) ,
    high_p decimal(20,2) ,
    low_p decimal(20,2) ,
    prev_close decimal(20,2),
    update_time datetime not null,
    currency varchar(10)
    );
    ''')
    cmd.execute('''
    create table stock_live(
    stock_code varchar(20) not null primary key,
    curr_p decimal(20,2) ,
    abs_change decimal(20,2) ,
    per_change decimal(20,2),
    update_time datetime not null,
    foreign key (stock_code) references stock_analysis(stock_code) on delete cascade
    );
        ''')
    cmd.execute('''
    create table users(
    user_id varchar(30) primary key,
    f_name varchar(20) not null,
    l_name varchar(20),
    email varchar(30) not null,
    pwd varchar(30) not null,
    acc_type varchar(20),
    fund decimal(20,2)
    );
        ''')
    cmd.execute('''
        create table gen_account(
        user_id varchar(30) primary key,
        per_stock varchar(20)
        );
            ''')
    cmd.execute('''
        create table pro_account(
        user_id varchar(30) primary key,
        per_year varchar(20)
        );
            ''')
    cmd.execute('''
        create table user_phone(
        user_id varchar(30) ,
        phone_number varchar(15)
        );
            ''')
    cmd.execute('''
    create table company(
    stock_code varchar(20) primary key,
    name varchar(40) not null,
    mkt_cap varchar(20),
    pe_ratio decimal(7,2),
    update_time datetime not null,
    foreign key (stock_code) references stock_analysis(stock_code) on delete cascade
    );
        ''')
    cmd.execute('''
    create table investment(
    user_id varchar(30) not null,
    stock_code varchar(20) not null,
    count int not null,
    primary key(user_id,stock_code),
    foreign key (stock_code) references stock_analysis(stock_code) on delete cascade,
    foreign key (user_id) references users(user_id) on delete cascade
    );
        ''')
    cmd.execute('''
    create table deal(
    stock_code varchar(20) primary key,
    buy int not null,
    sell int not null,
    foreign key (stock_code) references stock_analysis(stock_code) on delete cascade
    );
        ''')
    cmd.execute('''
    create table user_status(
    clientid varchar(20) primary key,
    userid varchar(20) not null,
    foreign key (userid) references users(user_id) on delete cascade
    );
        ''')


    cmd.execute('''
    insert into users(user_id,f_name,l_name,email,pwd,acc_type,fund) 
    values('admin','admin','admin','pythonstockproject@gmail.com','admin','professional',0)
    ''')
    cmd.execute('''
        insert into pro_account(user_id,per_year) 
        values('admin','50 USD')
        ''')
    cmd.execute('''
            insert into user_phone(user_id,phone_number) 
            values('admin','00')
            ''')
    cmd.execute('''
                insert into user_phone(user_id,phone_number) 
                values('admin','00')
                ''')
conn.close()
