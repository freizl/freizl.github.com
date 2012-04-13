
DECLARE
  r_enqueue_options      DBMS_AQ.ENQUEUE_OPTIONS_T;
  r_message_properties   DBMS_AQ.MESSAGE_PROPERTIES_T;
  v_message_handle       RAW(16);
  o_payload              SYS.AQ$_JMS_TEXT_MESSAGE;

BEGIN
  o_payload := SYS.AQ$_JMS_TEXT_MESSAGE.construct;
  o_payload.set_userid('demoq');
  o_payload.set_text('here is the message');

  DBMS_AQ.ADD_SUBSCRIBER(
    queue_name => 'esb_demo_queue',
    subscriber => sys.aq$_agent('recipient_1',null,null)
    );

  DBMS_AQ.ENQUEUE(
    queue_name =>  'esb_demo_queue',
    enqueue_options => r_enqueue_options,
    message_properties => r_message_properties,
    payload => o_payload,
    msgid => v_message_handle
    );

  COMMIT;

END;
/
