Components.utils.import("resource:///modules/virtualFolderWrapper.js");
Components.utils.import("resource://gre/modules/iteratorUtils.jsm");

Components.utils.import("resource:///modules/gloda/public.js");

// http://geekswithblogs.net/svanvliet/archive/2006/03/23/simple-javasc
// ript-object-dump-function.aspx
var MAX_DUMP_DEPTH = 10;
function dumpObj(obj, name, indent, depth) {
  if (depth > MAX_DUMP_DEPTH) {
    return indent + name + ": <Maximum Depth Reached>\n";
  }

  if (typeof obj == "object") {
    var child = null;
    var output = indent + name + "\n";
    indent += "\t";

    for (var item in obj) {
      try {
        child = obj[item];
      } catch (e) {
        child = "<Unable to Evaluate>";
      }

      if (typeof child == "object") {
        output += dumpObj(child, item, indent, depth + 1);
      } else {
        output += indent + item + ": " + child + "\n";
      }
    }
    return output;
  } else {
    return obj;
  }
}

/*
 * I don't know how to use namespace in JavaScript.  Let's use "nbt" as
 * a prefix for each function.  "nbt" stands for Notify By Tag.
 */
function nbt_run() {
  var output = document.getElementById('output');

  output.value = '555';

  
  let query = Gloda.newQuery(Gloda.NOUN_MESSAGE);

  query.folder(
    MailUtils.getFolderForURI(
      'mailbox://nobody@Local%20Folders/Expecting_Reply', true)
  );


  let myListener = {
    /* called when new items are returned by the database query or
    freshly indexed */
    onItemsAdded: function myListener_onItemsAdded(aItems, aCollection) {
    },
    /* called when items that are already in our collection get
    re-indexed */
    onItemsModified: function myListener_onItemsModified(aItems,
      aCollection) {
    },
    /* called when items that are in our collection are purged from the
    system */
    onItemsRemoved: function myListener_onItemsRemoved(aItems,
      aCollection) {
    },
    /* called when our database query completes */
    onQueryCompleted: function myListener_onQueryCompleted(aCollection)
    {
      let items = aCollection.items;
      let data = {
        messages: [],
      };
      for each (let [, glodaMsg] in Iterator(items)) {
        alert(glodaMsg.subject + ', ' + glodaMsg.from.value +
          ', ' + glodaMsg.to[0] + ', ' + glodaMsg.date);
        /*data.messages.push({
          subject: glodaMsg.subject,
          date: glodaMsg.date,
          author: glodaMsg.from.value,
        });*/
      };
    }
  };

  let collection = query.getCollection(myListener);
}
