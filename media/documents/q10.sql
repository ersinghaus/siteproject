
create table audit_log (
     PNO number(38),
     user_name varchar2(8),
     date_changed date,
     old_price float(63),
     new_price float(63)
);

create or replace trigger update_AuctionProperty
AFTER UPDATE OF reserve_price ON property_for_auction
set reserve_price = reserve_price - (reserve_price * .10)
where pno in ((select pno from property_for_auction)
      MINUS
      (select pno from deal)
);
   FOR EACH ROW 
     BEGIN
      insert into audit_log
       values (PNO number, user_name, date_changed, old_price, new_price);
     END;

select * from audit_log;

drop table audit_log;