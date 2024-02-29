/**
 * This file was auto-generated by Fern from our API Definition.
 */

package types;

import com.fasterxml.jackson.annotation.JsonValue;
import java.lang.String;

public enum Color {
  RED("red"),

  BLUE("blue");

  private final String value;

  Color(String value) {
    this.value = value;
  }

  @JsonValue
  @java.lang.Override
  public String toString() {
    return this.value;
  }
}