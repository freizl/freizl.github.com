
create or replace procedure testmessage AS
  msg SYS.AQ$_JMS_TEXT_MESSAGE;
  msg_hdr SYS.AQ$_JMS_HEADER;
  msg_agent SYS.AQ$_AGENT;
  msg_proparray SYS.AQ$_JMS_USERPROPARRAY;
  msg_property SYS.AQ$_JMS_USERPROPERTY;
  queue_options DBMS_AQ.ENQUEUE_OPTIONS_T;
  msg_props DBMS_AQ.MESSAGE_PROPERTIES_T;
  msg_id RAW(16);
  dummy VARCHAR2(4000);
begin
  msg_agent := SYS.AQ$_AGENT('subscriber_id', null, 0);
  msg_proparray := SYS.AQ$_JMS_USERPROPARRAY();
  msg_proparray.EXTEND(1);
  msg_property := SYS.AQ$_JMS_USERPROPERTY('JMS_OracleDeliveryMode', 100, '2', NULL, 27);
  msg_proparray(1) := msg_property;

  msg_hdr := SYS.AQ$_JMS_HEADER(msg_agent,null,'<USERNAME>',null,null,null,msg_proparray);
  msg := SYS.AQ$_JMS_TEXT_MESSAGE(msg_hdr,null,null,null);
  msg.text_vc := 'Hello from PL/SQL on XE';
  msg.text_len := length(msg.text_vc);
  DBMS_AQ.ENQUEUE( queue_name => 'esb_demo_queue'
                 , enqueue_options => queue_options
                 , message_properties => msg_props
                 , payload => msg
                 , msgid => msg_id);
end;
/
