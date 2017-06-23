/*
 * I don't know how to use namespace in JavaScript.  Let's use "nbt" as
 * a prefix for each function.  "nbt" stands for Notify By Tag.
 */
 
// [begin] Import statements.

// library for writing data into files
Components.utils.import("resource://gre/modules/osfile.jsm")

// Library to write log which you can read from Thunderbird's Error
// Console.
let consoleService = Components.classes["@mozilla.org/consoleservice;1"]
  .getService(Components.interfaces.nsIConsoleService);

// [end] Import statements.

// Dump JavaScript object.  This function is useful when we need to
// hack object in JavaScript.  Some times it is convenient to
// recursively dump all objects inside a specified object to see data
// inside in plaintext.
//
// References:
//   - http://geekswithblogs.net/svanvliet/archive/2006/03/23/simple-ja
//     vascript-object-dump-function.aspx
let NBT_MAX_DUMP_DEPTH = 10;
function nbt_dumpObj(obj, name, indent, depth) {
  if (depth > NBT_MAX_DUMP_DEPTH) {
    return indent + name + ": <Maximum Depth Reached>\n";
  }

  if (typeof obj == "object") {
    let child = null;
    let output = indent + name + "\n";
    indent += "\t";

    for (let item in obj) {
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
 * This function saves email subject, email author and email recipients
 * (email addresses in to: field) into file.
 *
 * Each line in the file is a text representation of a JSON object.
 * All JSON objects in text representation are separated by newline
 * character.
 */
function nbt_run() {
  // Get data from the current selected message.
  let selectednsIMsgDBHdr = gFolderDisplay.selectedMessage;
  // Use JSON format.
  let dataObj =
    {"subject" : selectednsIMsgDBHdr.mime2DecodedSubject,
     "author"  : selectednsIMsgDBHdr.mime2DecodedAuthor,
     "recipients": selectednsIMsgDBHdr.mime2DecodedRecipients 
    };
  let dataTxt = JSON.stringify(dataObj);

  // [begin] write data into a file
  //
  // references
  //   - https://developer.mozilla.org/en-US/docs/Mozilla/JavaScript_co
  //     de_modules/OSFile.jsm/OS.File_for_the_main_thread#OS.File.writ
  //     eAtomic

  // We have to encode string before writing into a file.
  // This encoder can be reused for several writes.
  let encoder = new TextEncoder();  

  let file = "/home/debian/tmp/nbt-data";
  OS.File.open(file, {write: true, append: true}).then(valOpen => {
    consoleService.logStringMessage('valOpen:', valOpen);
    let txtEncoded = new TextEncoder().encode(dataTxt + '\n');
    valOpen.write(txtEncoded).then(valWrite => {
        consoleService.logStringMessage('valWrite');
        valOpen.close().then(valClose => {
            consoleService.logStringMessage('valClose');
            consoleService.logStringMessage('successfully appended');
        });
    });
  });
  // [end] write data into a file
}
