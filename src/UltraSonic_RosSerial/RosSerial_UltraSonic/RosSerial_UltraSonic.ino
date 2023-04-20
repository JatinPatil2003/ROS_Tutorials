#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle  nh;

sensor_msgs::Range range_msg;
ros::Publisher pub_range( "/ultrasound", &range_msg);
char frameid[] = "/ultrasound";

const int trig_pin = 4;
const int echo_pin = 5;

void setup()
{
  Serial.begin(57600);
  nh.initNode();
  nh.advertise(pub_range);
  
  
  range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
  range_msg.header.frame_id =  frameid;
  range_msg.field_of_view = 0.1;  // fake
  range_msg.min_range = 0.0;
  range_msg.max_range = 500;
  
  pinMode(trig_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
  digitalWrite(trig_pin, LOW);
}

long distance(){
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  double duration = pulseIn(echo_pin,HIGH);
  double distance = duration * 0.034/2;
  Serial.println(distance);
  return distance;
}

void loop()
{
  range_msg.range = distance();
  range_msg.header.stamp = nh.now();
  pub_range.publish(&range_msg);
  nh.spinOnce();
  delay(500);
}
