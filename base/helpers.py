import random
import socket
import time
from django.db.models.fields import CharField
from django.utils.encoding import smart_unicode

class UIDField(CharField):
    empty_strings_allowed = False
    def __init__(self,verbose_name='UID', *args, **kwargs):
        assert kwargs.get('primary_key', False) is True, "%s must have primary_key=True." % self.__class__.__name__
        kwargs['blank'] = True
        kwargs['max_length'] = 20
        kwargs['editable'] = False
        super(UIDField,self).__init__(self, *args, **kwargs)

    @classmethod
    def create_uid(self):
      return u'%s' % UID()

    def pre_save(self,model_instance,add):
      if add:
        value = self.create_uid()
        setattr(model_instance,self.attname,value)
        return value
      else:
        return super(UIDField,self).pre_save(model_instance,add)
    
    def __unicode__(self):
        return 'UID'

class UID:
  '''A globally-unique identifier made up of time and 5 random digits: 35 characters wide

     A globally unique identifier that combines time, and random bits.  Since the
     time is listed first, you can sort records by guid.  You can also extract the time
     and ip if needed.
     GUIDs make wonderful database keys.  They require no access to the
     database (to get the max index number), they are extremely unique, and they sort
     automatically by time.   UIDs prevent key clashes when merging
     two databases together, combining data, or generating keys in distributed
     systems.
  '''
  rand = random.Random()
  lastuid = ''

  def __init__(self, uid=None):
    '''Constructor.  Use no args if you want the uid generated (this is the normal method)
       or send a string-typed uid to generate it from the string'''
    if uid is None:
      self.uid = self.__class__.lastuid
      while self.uid == self.__class__.lastuid:
        # time part
        now = long(time.time() * 1000)
        self.uid = ("%016x" % now)
        # random part
        self.uid += ("%03x" % (self.__class__.rand.randrange(0, 4095)))
      self.__class__.lastuid = self.uid

    elif type(uid) == type(self): # if a UID object, copy its value
      self.uid = str(uid)

    else: # if a string, just save its value
      assert self._check(uid), uid + " is not a valid UID!"
      self.uid = uid

  def __eq__(self, other):
      '''Return true if both GUID strings are equal'''
      if isinstance(other, self.__class__):
          return str(self) == str(other)
      return 0

  def __str__(self):
    '''Returns the string value of this guid'''
    return self.uid

  def time(self):
    '''Extracts the time portion out of the guid and returns the
       number of milliseconds since the epoch'''
    return long(self.guid[0:16], 16)


